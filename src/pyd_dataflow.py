import asyncio
import pandas as pd

class DataReader:
    def __init__(self, source):  # Source could be a file, socket, etc.
        self.source = source

    async def read(self):
        # Simulate reading data (e.g., from a CSV file)
        await asyncio.sleep(1)  # Simulate async I/O operation
        return pd.read_csv(self.source)

class Transformer:
    def transform(self, data):
        # Simple data transformation (e.g., normalizing a column)
        transformed_data = data.copy()
        if 'value' in transformed_data.columns:
            transformed_data['value'] = transformed_data['value'] / transformed_data['value'].max()
        return transformed_data

class Sink:
    def write(self, data):
        # Write logic (e.g., saving to a CSV file)
        data.to_csv('output.csv', index=False)

async def main():
    reader = DataReader('input.csv')
    transformer = Transformer()
    sink = Sink()

    data = await reader.read()
    transformed_data = transformer.transform(data)
    sink.write(transformed_data)

if __name__ == '__main__':
    asyncio.run(main())