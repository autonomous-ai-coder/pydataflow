# PyDataFlow

A lightweight streaming data processing framework designed for developers to handle real-time CSV and JSON ingestion, processing, and analysis efficiently while minimizing memory usage.

## Problem Solved
The challenge of processing large streaming datasets in real-time without overwhelming system resources, allowing developers to build data pipelines on low-resource machines.

## Scientific Background
### Theoretical Foundation
Based on stream processing principles and the Actor model for concurrency.

### Key Research Papers
- Jeffrey Dean and Sanjay Ghemawat. 'MapReduce: Simplified Data Processing on Large Clusters.'
- Martin Kleppmann. 'Designing Data-Intensive Applications.'


### Novel Aspects
- Lightweight processing model tailored for developers with limited resources.
- Integrated support for both CSV and JSON formats with minimal configuration.


## Hardware Requirements
### Minimum Requirements
- CPU: 2 cores, 2 GHz
- Memory: 2 GB RAM
- Storage: 500 MB available disk space
- GPU: None

### Recommended Requirements
- CPU: 4 cores, 3 GHz
- Memory: 8 GB RAM
- Storage: 1 GB available disk space
- GPU: None

## Resource Management
### Memory Optimization
Utilizes generator expressions for lazy loading of data, minimizing memory footprint while processing.

### CPU Optimization
Asynchronous I/O for non-blocking data reads and processing.

### Scaling Strategy
Can be deployed in clusters for distributed processing; scales horizontally.

### Fallback Mechanisms
Gracefully degrades to batch processing mode if resource constraints are detected.

## Technical Stack
### Core Libraries
- asyncio
- pandas
- fastjson


### Optimization Tools
- memory_profiler
- line_profiler


### Fallback Options
- Dask for larger dataset processing in a distributed manner


## Architecture
### Components
- Data Reader: For streaming data input from various sources.
- Transformer: For real-time data manipulation.
- Sink: For outputting processed data to desired destinations.


### Resource Usage
- Data Reader: Low memory usage - handles data in chunks.
- Transformer: Scales with input size; uses CPU for processing.
- Sink: Optimized to batch output efficiently.


### Optimization Points
- In the Data Reader by adjusting buffer size.
- In the Transformer by optimizing processing functions.


### Progressive Features
- Add multiple output sinks as resource availability increases.
- Implement parallel processing of transformations as CPU cores become available.


## Performance Metrics
- Memory usage during streaming
- Processing time for transformations
- Throughput of data processed per second


## Scaling Considerations
- Horizontal scaling supported via additional instances for increased throughput.
- Graceful handling of memory limits by switching to aggregated batch processing.


## Getting Started
[Installation and setup instructions will be added]

## Contributing
We welcome contributions! Please see our contributing guidelines.

## License
MIT License
