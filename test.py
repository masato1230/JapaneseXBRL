from app.parser import XBRLParser
from xml.etree import ElementTree


def test_tree_row_list(xbrl_file_path):
    """
    Test xbrl reading
    """
    xbrl_obj = ElementTree.parse(xbrl_file_path)
    root = xbrl_obj.getroot()
    row_list = []
    for child in root:
        row = [child.tag, child.attrib, child.text]
        row_list.append(row)
        
    return row_list

def test_iter(xbrl_file_path):
    """
    Test iter
    """
    xbrl_obj = ElementTree.parse(xbrl_file_path)
    root = xbrl_obj.getroot()
    for elem in root.getiterator():
        print(elem.tag, elem.attrib, elem.text)


if __name__ == '__main__':
    # row_list = test_read('/Users/m_ishikawa/Python/JapaneseXBRL/jpcrp030000-asr-001_E02265-000_2016-03-31_01_2016-06-30.xbrl')
    # print(row_list)
    test_iter('/Users/m_ishikawa/Python/JapaneseXBRL/jpcrp030000-asr-001_E02265-000_2016-03-31_01_2016-06-30.xbrl')
