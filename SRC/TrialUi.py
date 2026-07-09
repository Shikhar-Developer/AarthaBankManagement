import sys
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QHBoxLayout, 
    QVBoxLayout, QPushButton, QLabel, QTableWidget, 
    QTableWidgetItem, QStackedWidget, QHeaderView, QFrame
)
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont

class AdminDashboard(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Aartha Bank Management - Admin Console")
        self.resize(1100, 700) # Professional landscape aspect ratio

        # --- 1. MAIN SYSTEM SPLIT LAYOUT ---
        self.mainWidget = QWidget()
        self.mainLayout = QHBoxLayout(self.mainWidget)
        self.mainLayout.setContentsMargins(0, 0, 0, 0)
        self.mainLayout.setSpacing(0)
        self.setCentralWidget(self.mainWidget)

        # --- 2. THE NAVIGATION SIDEBAR PANEL ---
        self.sidebar = QFrame()
        self.sidebar.setFixedWidth(240)
        self.sidebar.setStyleSheet("""
            QFrame {
                background-color: #1A1D21; /* Darker than main layout workspace */
                border-right: 1px solid #2D3239;
                border-radius: 0px;
            }
            QPushButton {
                background-color: transparent;
                color: #A0AAB4;
                font-size: 14px;
                font-weight: 600;
                text-align: left;
                padding: 12px 20px;
                border: none;
                border-radius: 6px;
                margin: 4px 10px;
            }
            QPushButton:hover {
                background-color: #262B30;
                color: #FFFFFF;
            }
            QPushButton:checked {
                background-color: #0D6EFD; /* Accent Blue indicating active state */
                color: #FFFFFF;
            }
        """)

        # Sidebar Inner Widgets Layout
        self.sidebarLayout = QVBoxLayout(self.sidebar)
        self.sidebarLayout.setContentsMargins(0, 20, 0, 20)
        
        # Brand Logo Text header row
        self.brandLabel = QLabel("Aartha Admin Portal")
        self.brandLabel.setStyleSheet("font-size: 18px; font-weight: 800; color: #FFFFFF; padding: 0 20px 20px 20px;")
        self.sidebarLayout.addWidget(self.brandLabel)

        # Menu Buttons (Made checkable to group select focus)
        self.btnVerify = QPushButton("Verify Registrations")
        self.btnVerify.setCheckable(True)
        self.btnVerify.setChecked(True) # Defaults to first view tab active
        self.btnVerify.setCursor(Qt.CursorShape.PointingHandCursor)
        
        self.btnLogs = QPushButton("Database Logs")
        self.btnLogs.setCheckable(True)
        self.btnLogs.setCursor(Qt.CursorShape.PointingHandCursor)

        # Isolate selections using simple click connection exclusions
        self.btnVerify.clicked.connect(lambda: self.switch_tab(0, self.btnVerify))
        self.btnLogs.clicked.connect(lambda: self.switch_tab(1, self.btnLogs))

        self.sidebarLayout.addWidget(self.btnVerify)
        self.sidebarLayout.addWidget(self.btnLogs)
        self.sidebarLayout.addStretch() # Pushes everything to the top column line

        # --- 3. THE WORKSPACE PAGES CONTAINER ---
        self.workspace = QStackedWidget()
        self.workspace.setStyleSheet("background-color: #0F111A;") # Clean slate depth background

        # Page 1 View Setup: Verification Grid View
        self.pageVerify = QWidget()
        self.setup_verification_page()
        
        # Page 2 View Setup: System File Logs View
        self.pageLogs = QWidget()
        self.setup_logs_page()

        # Add pages down the slide stack index array
        self.workspace.addWidget(self.pageVerify)
        self.workspace.addWidget(self.pageLogs)

        # Assemble main split frames
        self.mainLayout.addWidget(self.sidebar)
        self.mainLayout.addWidget(self.workspace)

    def setup_verification_page(self):
        """Constructs a clean, styled table view row container."""
        layout = QVBoxLayout(self.pageVerify)
        layout.setContentsMargins(30, 30, 30, 30)

        title = QLabel("Pending Registration Approvals")
        title.setStyleSheet("font-size: 24px; font-weight: 700; color: #FFFFFF; background: transparent; margin-bottom: 5px;")
        
        subtitle = QLabel("The following customer registration tickets are awaiting administrative validation details.")
        subtitle.setStyleSheet("font-size: 13px; color: #A0AAB4; background: transparent; margin-bottom: 20px;")

        # --- MODERN TABLE STYLING ---
        self.userTable = QTableWidget(0, 3)
        self.userTable.setHorizontalHeaderLabels(["Ticket ID", "Full Name", "Mobile Number"])
        self.userTable.setSelectionBehavior(QTableWidget.SelectionBehavior.SelectRows)
        self.userTable.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)
        
        # Stretch columns layout to fill out space perfectly proportionally
        header = self.userTable.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(1, QHeaderView.ResizeMode.Stretch)
        header.setSectionResizeMode(2, QHeaderView.ResizeMode.Stretch)

        self.userTable.setStyleSheet("""
            QTableWidget {
                background-color: #1A1D21;
                border: 1px solid #2D3239;
                border-radius: 8px;
                gridline-color: #2D3239;
                color: #E3E6E8;
            }
            QHeaderView::section {
                background-color: #262B30;
                color: #FFFFFF;
                padding: 10px;
                font-weight: bold;
                border: none;
                border-bottom: 1px solid #2D3239;
            }
            QTableWidget::item {
                padding: 12px;
            }
            QTableWidget::item:selected {
                background-color: #0D6EFD;
                color: #FFFFFF;
            }
        """)

        layout.addWidget(title)
        layout.addWidget(subtitle)
        layout.addWidget(self.userTable)
        
        # Test Data injection visualization sample row hook
        self.add_table_row("PENDING_TK_1024", "Shikhar Chaturvedi", "+91 9999888877")

    def setup_logs_page(self):
        """Constructs the alternative tracking tab layout view."""
        layout = QVBoxLayout(self.pageLogs)
        layout.setContentsMargins(30, 30, 30, 30)
        
        title = QLabel("System Error Logs")
        title.setStyleSheet("font-size: 24px; font-weight: 700; color: #FFFFFF;")
        layout.addWidget(title)
        layout.addStretch()

    def add_table_row(self, ticket_id, name, mobile):
        """Helper action to seamlessly inject safe UI grid data variables."""
        row = self.userTable.rowCount()
        self.userTable.insertRow(row)
        self.userTable.setItem(row, 0, QTableWidgetItem(ticket_id))
        self.userTable.setItem(row, 1, QTableWidgetItem(name))
        self.userTable.setItem(row, 2, QTableWidgetItem(mobile))

    def switch_tab(self, index, active_button):
        """Handles slide swapping routing rules cleanly."""
        self.workspace.setCurrentIndex(index)
        # Clear selected check markings across unselected sidebar paths
        self.btnVerify.setChecked(active_button == self.btnVerify)
        self.btnLogs.setChecked(active_button == self.btnLogs)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AdminDashboard()
    window.show()
    sys.exit(app.exec())
