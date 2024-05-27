import widgets.main_widget.main_widget
import widgets.main_widget.ui_main_widget

def build_app():
    m_window = widgets.main_widget.main_widget.MainWidget(
        widgets.main_widget.ui_main_widget.Ui_mainWindow()
    )
    return m_window
