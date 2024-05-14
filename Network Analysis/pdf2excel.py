import tabula

input_file = "/Users/cosmowang/Documents/Win24/Network Analysis/Joint Ventures.pdf"
output = "joint venture.csv"

df = tabula.read_pdf(input_path=input_file, pages="all")
tabula.convert_into(input_path=input_file, output_path=output, 
                    output_format="csv", pages="all", stream=True)

