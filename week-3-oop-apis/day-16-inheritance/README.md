# DAY 16: Inheritance - Animal Hierarchy

## 📌 Problem Overview

Today you will learn:
1. What is Inheritance
2. Parent class and Child class
3. How to inherit methods using `class Child(Parent):`
4. Multi-level inheritance
5. Method overriding (optional)

### What is Inheritance?
- Child class gets all properties of Parent class
- Like child gets traits from parents
- Code reuse without rewriting

---

## 📚 Inheritance Hierarchy
- Animal (Grand Parent)
- ↑
- Mammal (Parent)
- ↑    ↑
- Dog Cat (Children)

Bird (Direct Child of Animal)

| Class | Inherits From | Has Methods |
|-------|---------------|-------------|
| Animal | None (Base) | `eat()`, `sleep()`, `info()` |
| Mammal | Animal | + `feed_milk()` |
| Dog | Mammal | + `bark()`, `wag_tail()` |
| Cat | Mammal | + `meow()`, `purr()` |
| Bird | Animal | + `fly()`, `lay_eggs()` |

---

## ❌ Common Errors & Solutions

### Error 1: Wrong inheritance syntax
```python
# WRONG ❌
def Mammal(Animal):  # 'def' not 'class'

# RIGHT ✅
class Mammal(Animal):  # 'class' is correct
```
### Error 2: Variable name typo
```
# WRONG ❌
print(f"🍼 {slf.name} feeds milk")  # 'slf' not 'self'

# RIGHT ✅
print(f"🍼 {self.name} feeds milk")
```
### Error 3: Class name typo
```py
# WRONG ❌
class Dog(Mamal):  # 'Mamal' missing 'm'

# RIGHT ✅
class Dog(Mammal):  # 'Mammal' correct
```
### Error 4: Missing self in method
```py
# WRONG ❌
def wag_tail(Mamal):  # Wrong parameter

# RIGHT ✅
def wag_tail(self):  # 'self' is correct
```
### Error 5: Wrong method name
```py
# WRONG ❌
tommy.infor()  # 'infor' not defined

# RIGHT ✅
tommy.info()  # 'info' is correct
```
### Error 6: Wrong method name
```py
# WRONG ❌
tommy.feed_mlk()  # 'feed_mlk' typo

# RIGHT ✅
tommy.feed_milk()  # 'feed_milk' correct
```
## 📚 Resources to Learn
Topic	Link
- Inheritance:	https://www.w3schools.com/python/python_inheritance.asp
- Method Overriding:	https://www.programiz.com/python-programming/method-overriding
- super() Function:	https://www.geeksforgeeks.org/python-super/


