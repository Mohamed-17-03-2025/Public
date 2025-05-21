using Microsoft.Win32;
using System;
using System.Drawing;
using System.IO;
using System.Windows;
using System.Windows.Media.Imaging;

namespace PDF_reader
{
    public partial class MainWindow : Window
    {
        private readonly PDFRenderer _renderer = new PDFRenderer();

        public MainWindow()
        {
            InitializeComponent();
        }

        private void OpenPDF_Click(object sender, RoutedEventArgs e)
        {
            OpenFileDialog openFileDialog = new OpenFileDialog
            {
                Filter = "PDF Files (*.pdf)|*.pdf"
            };
            if (openFileDialog.ShowDialog() == true)
            {
                try
                {
                    _renderer.LoadPDF(openFileDialog.FileName);
                    using (Bitmap? pageBitmap = _renderer.RenderPage(0))
                    {
                        if (pageBitmap != null)
                        {
                            PDFImage.Source = BitmapToImageSource(pageBitmap);
                        }
                        else
                        {
                            MessageBox.Show("Failed to render PDF page.", "Error", MessageBoxButton.OK, MessageBoxImage.Error);
                        }
                    }
                }
                catch (Exception ex)
                {
                    MessageBox.Show(ex.Message, "Error", MessageBoxButton.OK, MessageBoxImage.Error);
                }
            }
        }

        private BitmapImage BitmapToImageSource(Bitmap bitmap)
        {
            using (MemoryStream memory = new MemoryStream())
            {
                bitmap.Save(memory, System.Drawing.Imaging.ImageFormat.Png);
                memory.Position = 0;
                BitmapImage bitmapImage = new BitmapImage();
                bitmapImage.BeginInit();
                bitmapImage.StreamSource = memory;
                bitmapImage.CacheOption = BitmapCacheOption.OnLoad;
                bitmapImage.EndInit();
                return bitmapImage;
            }
        }
    }
}
