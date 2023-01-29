# File: est_tax.py

import doctest

def est_tax(taxable_income, tax_rate) -> float:
    """Generates an estimate for federal income tax and print the result

    Args:
        taxable_income: income after exemptions and deductions
        tax_rate: standard tax rate

    Returns:
    The tax owed for the provided taxable income and tax rate

    >>> est_tax(1000, .20)
    200.0
    """
    return taxable_income * tax_rate

def taxable(income: float, exemptions: int, exempt_amount: float, deduct_amount: float):
    """Adjust gross income to taxable income by applying the standard deduction and exemptions.

    Args:

        income: gross income, for which tax is being computed
        exemptions: number of personal exemptions
        exempt_amount: dollar amount for each exemption
        deduct_amount: dollar amount for standard deduction

    Returns:
        Taxable income dollar amount (int type)

    >>> taxable(43000, 1, 12550, 12550)
    17900
    """
    return income - deduct_amount - (exemptions * exempt_amount)

if __name__ == "__main__":
    EXEMPT_AMOUNT = 12550
    DEDUCT_AMOUNT = 12550
    TAX_RATE = 0.20

    doctest.testmod()
    income = float(input("Enter your income: "))
    exemptions = float(input("Enter number of exemptions: "))

    taxable_income = taxable(income, exemptions, EXEMPT_AMOUNT, DEDUCT_AMOUNT)
    print(f"Your taxable income is {taxable_income}")

    estimated_tax = est_tax(taxable_income, TAX_RATE)
    print(f"Based on that amount, your estimated tax is {estimated_tax}")
