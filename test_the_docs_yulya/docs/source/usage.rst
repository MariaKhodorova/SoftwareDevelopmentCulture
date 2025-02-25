Usage Guide
===========

Introduction
------------

Welcome to the usage guide for `utils_mix`. This guide provides examples and explanations on how to use the functions defined in the `utils_mix` Python module.

Importing the Module
--------------------

To start using `utils_mix`, you need to import it into your Python script or interactive session:

.. code-block:: python

   import utils_mix

Add and Multiply Numbers
------------------------

The `utils_mix` provides two simple functions for basic arithmetic operations:

- :func:`utils_mix.add_numbers`: Add two numbers together.
- :func:`utils.multiply_numbers`: Multiply two numbers.

Example usages:

.. code-block:: python

   # Import the module
   from utils_mix import add_numbers, multiply_numbers

   # Add two numbers
   result1 = add_numbers(1, 2)
   print("Result of addition:", result1)  # Output: 3

   # Multiply two numbers
   result2 = multiply_numbers(5, 6)
   print("Result of multiplication:", result2)  # Output: 30

Greet a Person
--------------

The `utils_mix` also provides a simple function to greet a person:

- :func:`utils_mix.greet`: Greet a person with a custom message.

Example usage:

.. code-block:: python

   # Import the module
   from utils_mix import greet

   # Greet a person
   greeting = greet("Alice")
   print(greeting)  # Output: Hello, Alice! How are you today?
