""" bootstrap your kervi dashboards here """
from kervi.dashboard import Dashboard, DashboardPanel

#Create the dashboards for your Kervi application here.
#Standard dashboard with several panels where sensors are placed.
#Each sensor create links to one or more dashboard panels
Dashboard(
    "app",
    "My dashboard",
    [
        DashboardPanel("light", title="Light"),
        DashboardPanel("sensors", title="Sensors")
    ],
    is_default=True
)

Dashboard(
    "system",
    "System",
    [
        DashboardPanel("cpu"),
        DashboardPanel("memory"),
        DashboardPanel("disk"),
        DashboardPanel("power", title="Power"),
        DashboardPanel("log", title="Log", user_log=True)
    ]
)
