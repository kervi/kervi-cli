""" bootstrap your kervi dashboards here """
from kervi.dashboard import Dashboard, Camboard, DashboardSection


MAIN = Camboard("cam", "Main", "cam1", is_default=True)
MAIN.add_section(DashboardSection("section1"))

SYSTEM = Dashboard("system", "System")
SYSTEM.add_section(DashboardSection("cpu", ui_columns=2))
SYSTEM.add_section(DashboardSection("memory", ui_columns=2))
SYSTEM.add_section(DashboardSection("disk", ui_columns=2))
