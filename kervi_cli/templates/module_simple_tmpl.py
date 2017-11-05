if __name__ == '__main__':
    from kervi.module import Module
    APP_MODULE = Module({{
        "info":{{
            "id":"{id}",
            "name":"{name}"
        }},
        "network":{{
            "IPAddress": "{module_ip}",
            "IPRootAddress": "{app_ip}",
            "IPCRootPort":{base_port},
        }}
    }})
    #Important GPIO must be imported after module creation
    from kervi.hal import GPIO

    from kervi.dashboard import Dashboard, DashboardPanel
    Dashboard(
        "module-{id}",
        "{{name}}",
        [
            DashboardPanel("light", title="Light")
        ],
        is_default=True
    )

    from kervi.sensor import Sensor
    from kervi_devices.platforms.common.sensors.memory_use import MemUseSensorDeviceDriver
    #build in sensor that measures cpu use
    SENSOR_1 = Sensor("MemUseSensor", "Memory", MemUseSensorDeviceDriver())
    #link to sys area top right
    SENSOR_1.link_to_dashboard("*", "sys-header")
    #link to a panel, show value in panel header and chart in panel body
    SENSOR_1.link_to_dashboard("module-{id}", "memory", type="value", link_to_header=True)
    SENSOR_1.link_to_dashboard("module-{id}", "memory", type="chart")


    #More on sensors https://kervi.github.io/sensors.html


    

    APP_MODULE.run()