### CLI for Rich-PyFiglet - A wrapper around Pyfiglet that renders output using Rich.
    
This lets you quickly try out what the fonts, colors, and animations look like
on your command line, or use it in your shell scripts. Rich-PyFiglet is also a library
you can import into your own python projects that are using Rich.
    
**Example usage** (Note the single quotes ''):
    
rich-pyfiglet hello   
rich-pyfiglet 'Hello World!' --font slant -j center    
rich-pyfiglet --colors red:green:blue -h 'Hello World!'   
rich-pyfiglet -c red:blue 'I <3 Rich' -a gradient_down    
rich-pyfiglet 'My CLI Tool' -c blue -b rounded -bc red    
    
Use `rich-pyfiglet figlet --help` to see all the options.