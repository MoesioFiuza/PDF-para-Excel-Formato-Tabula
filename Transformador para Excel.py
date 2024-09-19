import tabula
import pandas as pd

def pdf_to_excel(pdf_file, output_file):
    dfs = tabula.read_pdf(pdf_file, pages='all', multiple_tables=False)
    
    if dfs:
        with pd.ExcelWriter(output_file, engine='xlsxwriter') as writer:
            for i, df in enumerate(dfs):
        
                df.to_excel(writer, sheet_name=f'Página {i+1}', index=False)
    else:
        print("FUMO NOS PDFS")

pdf_file = r'C:\\Users\\moesios\\Desktop\\transporte público\\DEMANDA POR LINHA 0106 A 0806.pdf'
output_file = r'C:\\Users\\moesios\\Desktop\\transporte público\\DEMANDA POR LINHA 0106 A 0806.xlsx'

pdf_to_excel(pdf_file, output_file)
