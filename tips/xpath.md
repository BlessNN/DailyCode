### xpath介绍
XPath是一门可以再XML文档中查找信息的语言，通过tag元素和属性查找

### xpath语法
如：
<?xml version="1.0" encoding="ISO-8859-1"?>

<bookstore>

<book>
  <title lang="eng">Harry Potter</title>
  <price>29.99</price>
</book>

<book>
  <title lang="eng">Learning XML</title>
  <price>39.95</price>
</book>

</bookstore>

语法实例解释：
bookstore # 选取bookstore元素的所有子节点

/bookstore # 选取起始于根路径下的元素bookstore，比如/book则不匹配，因为根路径下没有book元素

bookstore/book # 选取bookstore/的book元素，如bookstore/title则不匹配

bookstore//title # 选取bookstore后代的所有title元素

//book # 选取所有book元素，不管位置

//@lang # 选取拥有属性lang的元素，即title元素

/bookstore/book[1]  # 选取bookstore的第一个book元素，/bookstore/book[last()]最后一个元素

//title[@lang='eng'] # 选取所有 title 元素，且这些元素拥有值为 eng 的 lang 属性

/bookstore/book[price>35.00] # 选取 bookstore 元素的所有 book 元素，且其中的 price 元素的值须大于 35.00

//title[@*] # 选取所有带有属性的 title 元素


