## Transformando lista en diccionario - 2

Para este ejercicio es importante documentarse de como python puede recibir un número `n` variable de argumentos con un solo parámetro.

Define la función `get_all_keys` que recibe como argumento uno o más diccionarios y regresa una lista de todas las claves `keys` de los diccionarios
recibidos.

Es importante desarrollar tu código usando `unittest` para verificar que tu programa se comporta y produce el resultado deseado.


```python
"""get_all_keys function goes here"""

...

```

```python
"""Ejemplo de entrada"""

person1 = {"name": "Fernando", "age": 34}
person2 = {"name": "Morelia", "age": 54}

print(get_all_keys(person1, person2))
>> ['name', 'age']
```

```
# unittest - TDD

$ python test_get_all_keys.py
```

> Tip: Se pueden obtener valores únicos con set.