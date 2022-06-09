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

[Source](https://realpython.com/python-exceptions/)

Exceptions are what handles an error occurrence in Python code. There are several built-in exceptions which are to be triggered when specific errors happen. But it's also available for coder to build own and customized exceptions to handle errors resulted by using their codes. Those exceptions could contain specific message so end-user would recognize the error occurred. The simplest form of exceptions usage is as follows...

    def division(divisor, dividend):
      if divisor == 0:
        raise Exception("Divisor can by any number but 0")

In above-case, exception was built to handle 1 very spaicifc error using if condition. But it also could be generalized to cover cases like function or whole process occurrence, just like below code...

    def remainder(divisor, dividend):
      try:
        result = int(dividend / divisor)
        multiply = result * divisor
        remainder = dividend - multiplied
      except:   // To be returned when error occurs in above function
        return "Something is wrong with your inputs for division operation."
      else:     // To be returned when no error occurs in above function
        return f'Division was successful and result is {remainder}'
      finally:  // To be always returned after any of "except" or "else" was triggered
        return "Thank you for using our app, you may refresh your page to use it again."
