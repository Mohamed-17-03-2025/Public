using MuPDFCore;
using System;
using System.Drawing;
using System.IO;

namespace PDF_reader
{
    public class PDFRenderer
    {
        private MuPDFContext? _context;
        private MuPDFDocument? _document;

        public void LoadPDF(string filePath)
        {
            try
            {
                _context = new MuPDFContext();
                _document = new MuPDFDocument(_context, filePath);
                Console.WriteLine("PDF loaded successfully");
            }
            catch (Exception ex)
            {
                _context?.Dispose();
                _context = null;
                _document = null;
                throw new Exception($"Failed to load PDF: {ex.Message}");
            }
        }

        public Bitmap? RenderPage(int pageNumber)
        {
            if (_document == null || pageNumber < 0 || pageNumber >= _document.Pages.Count)
                return null;

            try
            {
                
                string tempImagePath = Path.Combine(Path.GetTempPath(), $"page_{pageNumber}.png");// Temporary file path.

                
                _document.SaveImage// Save image to file.
                                   (pageNumber,
                                    1.0f,
                                    PixelFormats.RGBA,
                                    tempImagePath,
                                    RasterOutputFileTypes.PNG
                                   );

                
                return new Bitmap(tempImagePath);// Load the image as a Bitmap.
            }
            catch (Exception ex)
            {
                Console.WriteLine($"Render error: {ex.Message}");
                return null;
            }
        }

        public int PageCount => _document?.Pages.Count ?? 0;
    }
}
