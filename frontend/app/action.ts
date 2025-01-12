export async function solve(
  matrix2D: number[],
  matrix1D: number[],
  selectedForm: string,
): Promise<Error | number[]> {
  try {
    const response = await fetch(`http://127.0.0.1:8080/${selectedForm}`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        matrix_2d: matrix2D,
        matrix_1d: matrix1D,
      }),
    });

    if (!response.ok) {
      // Attempt to parse the error message from the server response
      const errorText = await response.text();
      return new Error(`Error: ${errorText || "Something went wrong!"}`);
    }

    const result = await response.json();
    return result;
  } catch (error) {
    return new Error(`Error: ${error}`);
  }
}
