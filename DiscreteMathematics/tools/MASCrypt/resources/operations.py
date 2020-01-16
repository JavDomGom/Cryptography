def addition(res, base, op1, op2, op3=None):
    import resources.Addition as la

    if op3 is None:
        res.set(
            la.Addition(base.get())
              .integerAddition(op1.get(), op2.get())
        )
    else:
        res.set(
            la.Addition(base.get())
              .modularAddition(op1.get(), op2.get(), op3.get())
        )


def substraction(res, base, op1, op2):
    import resources.Substraction as ls

    res.set(
        ls.Substraction(base.get())
          .integerSubtraction(op1.get(), op2.get())
    )


def multiplication(res, base, op1, op2):
    import resources.Multiplication as lm

    res.set(
        lm.Multiplication(base.get())
          .integerMultiplication(op1.get(), op2.get())
    )


def division(res, base, op1, op2):
    import resources.Division as ld

    res.set(
        ld.Division(base.get())
          .integerDivision(op1.get(), op2.get())
    )
