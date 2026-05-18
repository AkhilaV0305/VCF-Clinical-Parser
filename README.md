# VCF Clinical Variant Parser

A Python tool for parsing genomic VCF (Variant Call Format) files and generating clinical variant summary reports for precision medicine and clinical trial matching workflows.

## What is VCF?

VCF is the standard file format output from DNA sequencing labs. It contains:
- **CHROM**: Chromosome location
- **POS**: Genomic position  
- **REF**: Reference (normal) allele
- **ALT**: Alternate (variant) allele
- **QUAL**: Quality score (confidence in variant call)

Each row represents one genomic variant - a place where a patient's DNA differs from the normal reference genome.

## Clinical Application

Used in precision medicine workflows for:

1. **Pathologist Review** - Pathologists validate variants from sequencing labs
2. **Clinical Trial Matching** - Match patients to trials based on genomic profile (MatchMiner)
3. **Clinical Decision Support** - Integrate variants into EHR systems for clinician review

## Features

✓ Parse VCF 4.2 format files  
✓ Extract and validate variant records  
✓ Generate clinical summary statistics  
✓ Quality filtering and analysis  
✓ Export to CSV for downstream integration  

## Installation

```bash
pip install pandas
```

## Usage

```python
from vcf_parser import VCFParser

# Parse VCF and generate report
parser = VCFParser('sample.vcf')
report_df = parser.generate_report()

# Export to CSV
parser.export_csv('variants.csv')
```

## Example Output
