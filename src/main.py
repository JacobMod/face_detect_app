from window import Window, QtWidgets, sys


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main_window = QtWidgets.QMainWindow()
    main_widget = Window()
    main_window.setCentralWidget(main_widget)
    main_window.show()
    sys.exit(app.exec_())
