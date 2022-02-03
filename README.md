# LoriaPDF
A simple program to process pdfs, so they are printable as booklets.

LoriaPDF helps you to prepare your pdf for printing booklets. The result
should be easy to print on any A4 printer (Which supports double-sided 
printing). No more worrying which page should be where, everything will be
done automatically.

## Usage

You will need your pdf in portrait format.

The program can be used from the command line as follows:
```commandline
python main.py <input.pdf>
```
This will create an `output.pdf` in the same dictionary.

Now print the `output.pdf` on landscape DIN A4, double-sided (over the short
edge). After printing, just fold the hole pile in the middle and you get your
A5 booklet. If you want you can fix it with a stapler or any kind of binder.
Enjoy your booklet :D.

## Future plans

 - Create A6 Booklets to be printed in A4 and then cut.
 - Option to create two output files to support printers which can't print double-sided
   automatically.
 - GUI so everybody can use it.

## Requirements

`pikepdf` is required. For most people `pip install pikepdf` will do.
For further installation details check 
https://pikepdf.readthedocs.io/en/latest/installation.html. `pikepdf` is
licensed under MPL 2.0 .
