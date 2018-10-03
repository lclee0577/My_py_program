from pywinauto.application import Application
# Run a target application
app = Application().connect(title_re="迅雷U享版", class_name="XLUEFrameHostWnd")
# print(app.Properties.print_control_identifiers())
app.window(handle=0x02087c)
app.YourDialog.print_control_identifiers()# dlg = app.top_window()
print('123')