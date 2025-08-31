```sh
$> python filterstring.py 'Hello the World' 4
['Hello', 'World']
$>
```

```sh
$> python filterstring.py 'Hello the World' 99
[]
$>
```

```sh
$> python filterstring.py 3 'Hello the World'
AssertionError: the arguments are bad
$>
```

```sh
$> python filterstring.py
AssertionError: the arguments are bad
$>
```