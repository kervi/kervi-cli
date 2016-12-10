""" My kervi application """
from kervi.bootstrap import Application
import kervi.utility.nethelper as nethelper

if __name__ == '__main__':
    APP = Application({{
        "info":{{
            "id":"{id}",
            "name":"{name}",
            "appKey":"",
        }},
        "log" : {{
            "level":"debug",
            "file":"{log}.log"
        }},
        "modules":["sensors", "controllers"],
        "network":{{
            "IPAddress": nethelper.get_ip_address(),
            "IPCBasePort":{base_port},
            "WebSocketPort":{websocket_port},
            "WebPort": {ui_port},
            "IPCSecret":b"{secret}"
        }},
    }})
    
    APP.run()