import pandas as pd

class VCFParser:
    def __init__(self, vcf_file):
        self.vcf_file = vcf_file
        self.variants = []
    
    def parse_vcf(self):
        """Parse VCF file and extract variant records"""
        with open(self.vcf_file, 'r') as f:
            for line in f:
                # Skip header lines
                if line.startswith('##'):
                    continue
                if line.startswith('#CHROM'):
                    continue
                
                # Parse variant lines
                fields = line.strip().split('\t')
                if len(fields) >= 8:
                    variant = {
                        'chromosome': fields[0],
                        'position': fields[1],
                        'reference_allele': fields[3],
                        'alternate_allele': fields[4],
                        'quality_score': float(fields[5]) if fields[5] != '.' else 0,
                        'filter': fields[6]
                    }
                    self.variants.append(variant)
        
        return pd.DataFrame(self.variants)
    
    def generate_report(self):
        """Generate clinical summary report"""
        df = self.parse_vcf()
        
        print("\n" + "="*60)
        print("CLINICAL VARIANT SUMMARY REPORT")
        print("="*60)
        print(f"\nTotal Variants: {len(df)}")
        print(f"Chromosomes Affected: {df['chromosome'].nunique()}")
        print(f"High Quality Variants (QUAL > 30): {len(df[df['quality_score'] > 30])}")
        
        print("\n--- Variants by Chromosome ---")
        print(df['chromosome'].value_counts().sort_index().to_string())
        
        print("\n--- Quality Score Statistics ---")
        print(f"Mean Quality: {df['quality_score'].mean():.2f}")
        print(f"Min Quality: {df['quality_score'].min():.2f}")
        print(f"Max Quality: {df['quality_score'].max():.2f}")
        
        print("\n" + "="*60)
        
        return df
    
    def export_csv(self, output_file='variant_report.csv'):
        """Export variant data to CSV"""
        df = self.parse_vcf()
        df.to_csv(output_file, index=False)
        print(f"✓ Report exported to {output_file}")
        return df

if __name__ == "__main__":
    parser = VCFParser('sample.vcf')
    df = parser.generate_report()
    parser.export_csv()
