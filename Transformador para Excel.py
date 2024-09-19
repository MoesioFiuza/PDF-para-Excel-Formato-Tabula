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

pdf_file = r'caminho pdf.pdf'
output_file = r'caminho de saída para excel.xlsx'

pdf_to_excel(pdf_file, output_file)
