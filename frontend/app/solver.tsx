"use client";

import { useState, useEffect } from "react";
import { Button } from "@/components/ui/button";
import { Card, CardContent } from "@/components/ui/card";
import { Label } from "@/components/ui/label";
import { Textarea } from "@/components/ui/textarea";
import {
  Select,
  SelectTrigger,
  SelectContent,
  SelectItem,
} from "@/components/ui/select";
import { Switch } from "@/components/ui/switch"; // Assuming you have a Switch component

const IndexPage = () => {
  const [matrix2d, setMatrix2d] = useState<string>(""); // Text input for 2D matrix
  const [matrix1d, setMatrix1d] = useState<string>(""); // Text input for 1D matrix
  const [result, setResult] = useState<number[] | null>(null);
  const [selectedForm, setSelectedForm] = useState<string>("smith");
  const [useTableInput2d, setUseTableInput2d] = useState<boolean>(false);
  const [useTableInput1d, setUseTableInput1d] = useState<boolean>(false);
  const [matrix2dTable, setMatrix2dTable] = useState<number[][]>([
    [0, 0],
    [0, 0],
  ]);
  const [matrix1dTable, setMatrix1dTable] = useState<number[]>([0, 0]);

  // Sync table data to text when switching to text mode
  useEffect(() => {
    if (!useTableInput2d) {
      setMatrix2d(JSON.stringify(matrix2dTable));
    }
  }, [useTableInput2d, matrix2dTable]);

  // Sync text input to table data when switching to table mode
  useEffect(() => {
    if (useTableInput2d && matrix2d) {
      try {
        const parsedMatrix: number[][] = JSON.parse(matrix2d);
        // Ensure matrix is square
        const size = parsedMatrix.length;
        for (let row of parsedMatrix) {
          if (row.length !== size) {
            console.error("Matrix is not square");
            return;
          }
        }
        setMatrix2dTable(parsedMatrix);
      } catch (error) {
        console.error("Invalid 2D matrix format", error);
      }
    }
  }, [matrix2d, useTableInput2d]);

  // Sync table data to text when switching to text mode for 1D matrix
  useEffect(() => {
    if (!useTableInput1d) {
      setMatrix1d(JSON.stringify(matrix1dTable));
    }
  }, [useTableInput1d, matrix1dTable]);

  // Sync text input to table data when switching to table mode for 1D matrix
  useEffect(() => {
    if (useTableInput1d && matrix1d) {
      try {
        const parsedMatrix: number[] = JSON.parse(matrix1d);
        setMatrix1dTable(parsedMatrix);
      } catch (error) {
        console.error("Invalid 1D matrix format", error);
      }
    }
  }, [matrix1d, useTableInput1d]);

  // Ensure the size of 2D matrix and 1D matrix are always the same
  const handleMatrix2dChange = (e: React.ChangeEvent<HTMLTextAreaElement>) => {
    setMatrix2d(e.target.value);
  };

  const handleMatrix1dChange = (e: React.ChangeEvent<HTMLTextAreaElement>) => {
    setMatrix1d(e.target.value);
  };

  const handleSelectChange = (value: string) => {
    setSelectedForm(value);
  };

  const handleTableChange = (value: number, row: number, col: number) => {
    const updatedMatrix = [...matrix2dTable];
    updatedMatrix[row][col] = value;
    setMatrix2dTable(updatedMatrix);

    // Ensure the 1D matrix length matches the 2D matrix rows
    if (updatedMatrix.length !== matrix1dTable.length) {
      setMatrix1dTable(new Array(updatedMatrix.length).fill(0));
    }
  };

  const handleMatrix1dTableChange = (value: number, index: number) => {
    const updatedMatrix = [...matrix1dTable];
    updatedMatrix[index] = value;
    setMatrix1dTable(updatedMatrix);
  };

  const handleSubmit = async () => {
    try {
      let matrix2dParsed;
      let matrix1dParsed;

      if (useTableInput2d) {
        matrix2dParsed = matrix2dTable;
      } else {
        matrix2dParsed = JSON.parse(matrix2d);
      }

      if (useTableInput1d) {
        matrix1dParsed = matrix1dTable;
      } else {
        matrix1dParsed = JSON.parse(matrix1d);
      }

      // Validate that the number of rows in 2D matrix equals the length of 1D matrix
      if (matrix2dParsed.length !== matrix1dParsed.length) {
        alert(
          "Matrix sizes do not match! The number of rows in the 2D matrix must equal the length of the 1D matrix.",
        );
        return;
      }

      const response = await fetch(`http://127.0.0.1:5000/${selectedForm}`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          matrix_2d: matrix2dParsed,
          matrix_1d: matrix1dParsed,
        }),
      });

      if (!response.ok) {
        const errorData = await response.json();
        console.error(errorData);
        throw new Error(errorData.error);
      }

      const data = await response.json();
      setResult(data.result_matrix);
    } catch (error) {
      console.error(error);
    }
  };

  return (
    <div className="flex justify-center items-center h-screen bg-gray-100">
      <Card className="w-96 p-4">
        <CardContent>
          <h2 className="text-2xl font-bold mb-4">
            Linear Diophantine Equation Solver
          </h2>

          {/* 2D Matrix Input Toggle */}
          <div className="mb-4 flex items-center">
            <Label className="mr-2">2D Matrix Input (Table/Text):</Label>
            <Switch
              checked={useTableInput2d}
              onCheckedChange={(checked) => setUseTableInput2d(checked)}
            />
          </div>

          {useTableInput2d ? (
            <>
              <div className="mb-4">
                <Label>2D Matrix (Table Input):</Label>
                <table className="w-full mt-2">
                  <tbody>
                    {matrix2dTable.map((row, rowIndex) => (
                      <tr key={rowIndex}>
                        {row.map((col, colIndex) => (
                          <td key={colIndex} className="px-2 py-1 border">
                            <input
                              type="number"
                              value={col}
                              onChange={(e) =>
                                handleTableChange(
                                  Number(e.target.value),
                                  rowIndex,
                                  colIndex,
                                )
                              }
                              className="w-full"
                            />
                          </td>
                        ))}
                      </tr>
                    ))}
                  </tbody>
                </table>
              </div>
            </>
          ) : (
            <>
              <div className="mb-4">
                <Label htmlFor="matrix2d">2D Matrix (Text Input):</Label>
                <Textarea
                  id="matrix2d"
                  value={matrix2d}
                  onChange={handleMatrix2dChange}
                  placeholder="[[1,2],[3,4]]"
                  rows={5}
                  className="mt-2"
                />
              </div>
            </>
          )}

          {/* 1D Matrix Input Toggle */}
          <div className="mb-4 flex items-center">
            <Label className="mr-2">1D Matrix Input (Table/Text):</Label>
            <Switch
              checked={useTableInput1d}
              onCheckedChange={(checked) => setUseTableInput1d(checked)}
            />
          </div>

          {useTableInput1d ? (
            <>
              <div className="mb-4">
                <Label>1D Matrix (Table Input):</Label>
                <div className="flex gap-2">
                  {matrix1dTable.map((value, index) => (
                    <input
                      key={index}
                      type="number"
                      value={value}
                      onChange={(e) =>
                        handleMatrix1dTableChange(Number(e.target.value), index)
                      }
                      className="w-20 border"
                    />
                  ))}
                </div>
              </div>
            </>
          ) : (
            <>
              <div className="mb-4">
                <Label htmlFor="matrix1d">1D Matrix (Text Input):</Label>
                <Textarea
                  id="matrix1d"
                  value={matrix1d}
                  onChange={handleMatrix1dChange}
                  placeholder="[1,2]"
                  rows={3}
                  className="mt-2"
                />
              </div>
            </>
          )}

          <div className="mb-4">
            <Label htmlFor="formSelect">Choose the Form:</Label>
            <Select onValueChange={handleSelectChange} value={selectedForm}>
              <SelectTrigger className="mt-2">
                <span>
                  {selectedForm === "smith"
                    ? "Smith Normal Form"
                    : "Hermite Normal Form"}
                </span>
              </SelectTrigger>
              <SelectContent>
                <SelectItem value="smith">Smith Normal Form</SelectItem>
                <SelectItem value="hermite">Hermite Normal Form</SelectItem>
              </SelectContent>
            </Select>
          </div>

          <Button className="w-full mb-4" onClick={handleSubmit}>
            Solve
          </Button>

          {result && (
            <div className="mt-4">
              <h3 className="text-xl font-bold">Result:</h3>
              <ul>
                {result.map((value, index) => (
                  <li key={index}>
                    X{index + 1} = {value.toFixed(2)}
                  </li>
                ))}
              </ul>
            </div>
          )}
        </CardContent>
      </Card>
    </div>
  );
};

export default IndexPage;