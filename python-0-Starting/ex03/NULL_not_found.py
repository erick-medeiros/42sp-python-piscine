def NULL_not_found(object: any) -> int:
    if isinstance(object, type(None)):
        print("Nothing: None", type(None))
    elif isinstance(object, float) and object != object:
        print("Cheese: nan", type(object))
    elif isinstance(object, bool) and object is False:
        print("Fake: False", type(object))
    elif isinstance(object, int) and object == 0:
        print("Zero: 0", type(object))
    elif isinstance(object, str) and len(object) == 0:
        print("Empty:", type(object))
    else:
        print("Type not found")
    return 1
