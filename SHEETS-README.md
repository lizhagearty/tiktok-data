## Google Sheets Formulas 

#### to get sum of column b cells where column a for that row = yes 

In Excel, you can use the SUMIF function to sum the values in a range based on a given criterion. For example, if you want to sum the values in column B where the corresponding cell in column A is "yes", you can use the following formula:

```
=SUMIF(A:A, "yes", B:B)
```

This will sum the values in column B for all rows where the corresponding cell in column A is "yes".

Here is how the SUMIF function works:

A:A is the range of cells in column A to check.
"yes" is the criterion to check for. In this case, we are checking for cells that contain the text "yes".
B:B is the range of cells in column B that will be summed.
You can also use the SUMIFS function to sum values based on multiple criteria. For example, to sum the values in column B where the corresponding cell in column A is "yes" and the corresponding cell in column C is "red", you can use the following formula:

```
=SUMIFS(B:B, A:A, "yes", C:C, "red")
```

This will sum the values in column B for all rows where the corresponding cell in column A is "yes" and the corresponding cell in column C is "red".

#### get total of values across several sheet tabs in google sheets

To get the total of values across several sheet tabs in Google Sheets, you can use the SUM function and reference the cells in the other sheet tabs using the sheet name and cell address.

For example, if you want to sum the values in cell A1 of sheet1, sheet2, and sheet3, you can use the following formula:

```=SUM(sheet1!A1, sheet2!A1, sheet3!A1)```

This will add the values in cell A1 of each sheet and give you the total.

You can also use the SUM function to sum a range of cells across sheet tabs. For example, if you want to sum the values in cells A1:A10 of sheet1, sheet2, and sheet3, you can use the following formula:

```=SUM(sheet1!A1:A10, sheet2!A1:A10, sheet3!A1:A10)```
This will add the values in cells A1:A10 of each sheet and give you the total.

Note that the sheet names are case-sensitive, so make sure to use the correct capitalization. Also, make sure to include the ! symbol between the sheet name and the cell address.