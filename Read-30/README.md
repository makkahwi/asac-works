# Lesson 30 Reading

Navigation | [Past Reading](../Read-29/README.md) | [Home Page](../README.md) | [Next Reading](../Read-31/README.md) |

## Intro to Hash Tables

[Source](https://codefellows.github.io/common_curriculum/data_structures_and_algorithms/Code_401/class-30/resources/Hashtables.html)
[Source](https://www.youtube.com/watch?v=MfhjkfocRR0)
[Source](https://www.hackerearth.com/practice/data-structures/hash-tables/basics-of-hash-tables/tutorial/)
[Source](https://en.wikipedia.org/wiki/Hash_table)

HashTables are a data structures used to encrypting & protecting data. Data is to be stored in HashTables in form of pairs, where a pair contains a key and a value & they allow to have multiple values associated with the same hashed key. So in a way, hashtable is sort of a list of lists, as it's a list of hashed keys, and each hashed key got a list of pairs of keys & binded values.

HashTables tables are to be built as a Class in python, where it's default methods are

- Add() | to add a paired data to the HashTable.
- Find() | to return the corresponding values of a key.
- Contains() | to check if a key exists in the HashTable.
- Hash() | to hash a key n return a hashed key.

The process to add data to hashtable (Add method structure) is basically to...

- Hash the key of the data to be stored (using Hash method). Which is to be done by converting the key text into an integer value and multiply it by a prime integer to get the hashed key value.
- Then the HashTable is to be checked if generated hashed key exists in the table or not (using Contains method).
- If not, a new list of pairs is to be added to the hashed key, including the new data pair to be stored.
- If the hashed key was found in the HashTable, the new pair is to be appended to the existing list of pairs (this is was is called a collision case).
