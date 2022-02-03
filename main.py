# This is a sample Python script.
import sys

from pikepdf import Pdf, Page, Name, Rectangle


def to_one_page(pdf: Pdf, left: int, right: int, n: int = None) -> Page:
    """
    Put's the to pages of given index onto one page which will be appended at
    the end of the document.

    Note: Input pages should be in portrait format, output page is in
    landscape format. DIN A4 is used for the added page.

    :param pdf: The document which will be manipulated.
    :param left: The index of the page that should be placed left.
    :param right: The index of the page that should be placed right.
    :param n: Maximal page index which should be used for source pages.
        (default: #pages in pdf)
    :return: A reference to the new added Page.
    """
    if n is None:
        n = len(pdf.pages)
    blank_page = pdf.add_blank_page(page_size=(842, 595))

    if left < n:
        left_page = Page(pdf.pages[left])
        blank_page.add_overlay(left_page, Rectangle(0, 0, 421, 595))

    if right < n:
        right_page = Page(pdf.pages[right])
        blank_page.add_overlay(right_page, Rectangle(421, 0, 842, 595))

    return blank_page


def make_booklet(pdf: Pdf, delete_old_pages: bool = True):
    """
    Rearranges the pages so they can be printed as a booklet.

    The output will an landscape DIN A4 pdf.

    :param pdf: The document which will be manipulated.
    :param delete_old_pages: If True, old pages will be removed from the
        document. (default: True)
    :return: None
    """
    n_original = len(pdf.pages)
    n = n_original + (4 - (n_original % 4)) % 4
    for i in range(0, n // 2, 2):
        to_one_page(pdf, n - i - 1, i, n_original)  # front
        to_one_page(pdf, i + 1, n - i - 2, n_original)  # back
    if delete_old_pages:
        del pdf.pages[:n_original]


if __name__ == '__main__':
    if len(sys.argv) <= 1:
        print("Input file needed")
        sys.exit()
    with Pdf.open(sys.argv[1]) as pdf:
        make_booklet(pdf)
        pdf.save('output.pdf')
