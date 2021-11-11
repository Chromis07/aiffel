def test_generator():
    yield print("1")
    yield print("1")
    yield print("1")


gen = test_generator()

next(gen)
