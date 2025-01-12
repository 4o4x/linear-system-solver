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
import { Switch } from "@/components/ui/switch";
import { toast } from "react-toastify";

const IndexPage = () => {
  const [matrix2d, setMatrix2d] = useState<string>(""); // Text input for 2D matrix
  const [matrix1d, setMatrix1d] = useState<string>(""); // Text input for 1D matrix
  const [result, setResult] = useState<number[] | null>(null);
  const [selectedForm, setSelectedForm] = useState<string>("smith");
  const [useTableInput, setUseTableInput] = useState<boolean>(false); // Single switch for both matrices
  const [matrix2dTable, setMatrix2dTable] = useState<number[][]>([
    [0, 0],
    [0, 0],
  ]);
  const [matrix1dTable, setMatrix1dTable] = useState<number[]>([0, 0]);
  const [size, setSize] = useState<number>(2); // Single size input for both 2D matrix rows and columns

  // Sync table data to text when switching to text mode
  useEffect(() => {
    if (!useTableInput) {
      setMatrix2d(JSON.stringify(matrix2dTable));
      setMatrix1d(JSON.stringify(matrix1dTable));
    }
  }, [useTableInput, matrix2dTable, matrix1dTable]);

  useEffect(() => {
    if (useTableInput) {
      const parsedMatrix2d = JSON.parse(matrix2d);
      const parsedMatrix1d = JSON.parse(matrix1d);
 
      // Add new rows to the 2D matrix
      // If the size is smaller than the current matrix size, remove the extra rows
      // If the size is larger than the current matrix size, add new rows and columns with 0 values
 
      const updatedMatrix2d = parsedMatrix2d
        .slice(0, size)
        .map((row, rowIndex) => {
          if (row.length < size) {
            return [...row, ...new Array(size - row.length).fill(0)];
          } else {
            return row.slice(0, size);
          }
        });
 
      if (parsedMatrix2d.length < size) {
        updatedMatrix2d.push(
          ...new Array(size - parsedMatrix2d.length).fill(
            new Array(size).fill(0),
          ),
        );
      }
 
      setMatrix2dTable(updatedMatrix2d);
 
      // Ensure the 1D matrix length matches the 2D matrix rows
      // If the size is smaller than the current matrix size, remove the extra values
      // If the size is larger than the current matrix size, add new values with 0 values
 
      const updatedMatrix1d = parsedMatrix1d.slice(0, size);
      if (parsedMatrix1d.length < size) {
        updatedMatrix1d.push(
          ...new Array(size - parsedMatrix1d.length).fill(0),
        );
      }
      setMatrix1dTable(updatedMatrix1d);
    }
  }, [useTableInput, matrix2d, matrix1d, size]);
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

      if (useTableInput) {
        matrix2dParsed = matrix2dTable;
        matrix1dParsed = matrix1dTable;
      } else {
        matrix2dParsed = JSON.parse(matrix2d);
        matrix1dParsed = JSON.parse(matrix1d);
      }

      // Validate that the number of rows in 2D matrix equals the length of 1D matrix
      if (matrix2dParsed.length !== matrix1dParsed.length) {
        alert(
          "Matrix sizes do not match! The number of rows in the 2D matrix must equal the length of the 1D matrix.",
        );
        return;
      }

      const response = await fetch(`http://127.0.0.1:8080/${selectedForm}`, {
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
        // Attempt to parse the error message from the server response
        const errorText = await response.text();
        toast(`Error: ${errorText || "Something went wrong!"}`);
        return;
      }

      const data = await response.json();
      setResult(data.result_matrix);
      toast("Submission successful!");
    } catch (error) {
      // Log the error and display the error message using toast
      console.error("Error:", error);
      toast(`Error: ${error.message || "Something went wrong!"}`);
    }
  };

  return (
    <div className="flex justify-center items-center h-screen bg-gray-100">
      <Card className="p-4">
        <CardContent>
          <h2 className="text-2xl font-bold mb-4">
            Linear Diophantine Equation Solver
          </h2>

          {/* Single size input */}
          <div className="mb-4 flex items-center">
            <Label className="mr-2 text-sm">Matrix Size:</Label>
            <input
              type="number"
              min={1}
              value={size}
              onChange={(e) => setSize(Number(e.target.value))}
              className="w-16 p-2 text-sm border"
            />
          </div>

          {/* Single switch for both matrices */}
          <div className="mb-4 flex items-center">
            <Label className="mr-2">Toggle Input (Text/Table):</Label>
            <Switch
              checked={useTableInput}
              onCheckedChange={(checked) => setUseTableInput(checked)}
            />
          </div>

          {/* 2D Matrix Input (Table/Text) */}
          {useTableInput ? (
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

          {/* 1D Matrix Input (Table/Text) */}
          {useTableInput ? (
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
