from UIFactory import WinUIFactory, MacUIFactory

def main(type):
    if type == 'win':
        factory = WinUIFactory()
    elif type == 'mac':
        factory = MacUIFactory()
    else:
        raise ValueError('Unknown OS type')
    
    button = factory.create_button()
    textbox = factory.create_textbox()

    button.press()
    textbox.press()


if __name__ == "__main__":
    _input = 'win'
    main(_input)
    
# Output
# Windows Button    
# Windows Textbox

# Mac Button
# Mac Textbox

