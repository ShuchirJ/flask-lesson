If you write a for loop like this in Python:
```python
for variable in list:
    print(variable)
```

you can use it like this in HTML:

```html
{% for variable in list %}
<p>{{ variable }}</p>
{% endfor %}
```

Example:

in Python:
```python
fruits = ["apple", "banana", "mango"]
for fruit in fruits:
    print(fruit)
```

in HTML:
```
{% for fruit in fruits %}
<p>{{ fruit }}</p>
{% endfor %}
```

For this to work, you need to make fruits a list in Python first then a variable in HTML like I made `name` a variable in [`app.py`](/app.py) on line 13.