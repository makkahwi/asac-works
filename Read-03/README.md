# Lesson 3 Reading

Navigation | [Past Reading](../Read-02/README.md) | [Home Page](../README.md) | [Next Reading](../Read-04/README.md) |

## Read & Write Files in Python

[Source](https://realpython.com/read-write-files-python/)

Files are basically containers to hold & store data. This data is formatted in a specific way of any sorts like texts, images, videos & exe software. Of course all of this data is translated into PC language of binaries. File is constructed in the major parts, headers to hold metadata, content fed by user and EOF which signals the file ending.

In python, there are built-in functions to deal with external files like...

    file = open('./assets/docs/data.txt', 'r')      // to read only
    file = open('./assets/docs/data.txt', 'w')      // to write
    file = open('./assets/docs/data.txt', 'rb')     // to read in binary
    file = open('./assets/docs/data.txt', 'wb')     // to write in binary
    file.close()                                    // to close the file

---

## Exceptions in Python

[Source](https://realpython.com/python-exceptions//)

Text
