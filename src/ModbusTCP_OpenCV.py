import argparse
from pyModbusTCP.server import ModbusServer, DataBank, DataHandler 
from datetime import datetime
from HandTracking_MobusTCP import handTracking

class MyDataBank(DataBank):
    def __init__(self,handTracking):
        super().__init__(virtual_mode=True)
        self.data = handTracking

    def get_holding_registers(self, address, number=1, srv_info=None):
        """Get virtual holding registers."""
        now = datetime.now()
        percent  = self.data.outputData()
        v_regs_d = {0: now.day, 1: now.month, 2: now.year,
                    3: now.hour, 4: now.minute, 5: now.second,
                    7: percent}
        try:
            return [v_regs_d[a] for a in range(address, address+number)]
        except KeyError:
            return
if __name__ == '__main__':
    handTrack = handTracking(0)
    parser = argparse.ArgumentParser()
    parser.add_argument('-H', '--host', type=str, default='localhost', help='Host (default: localhost)')
    parser.add_argument('-p', '--port', type=int, default=502, help='TCP port (default: 502)')
    args = parser.parse_args()
    # init modbus server and start it
    server = ModbusServer(host=args.host, port=args.port,no_block = True, data_bank = MyDataBank(handTrack))
    print(f"[+]info : Server is Online on IP : {args.host} and PORT : {args.port} ")
    server.start()
    while True:
        handTrack.videoCapture()
     

       
        

  
