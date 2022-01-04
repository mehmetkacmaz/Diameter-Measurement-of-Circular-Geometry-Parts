/*----------------------------------------------------------------------------

  I/O functions: read PGM or ASC images and curve output to PDF or TXT files.

  Copyright (c) 2016-2017 rafael grompone von gioi <grompone@gmail.com>,
                          Gregory Randall <randall@fing.edu.uy>

  This program is free software: you can redistribute it and/or modify
  it under the terms of the GNU Affero General Public License as
  published by the Free Software Foundation, either version 3 of the
  License, or (at your option) any later version.

  This program is distributed in the hope that it will be useful,
  but WITHOUT ANY WARRANTY; without even the implied warranty of
  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
  GNU Affero General Public License for more details.

  You should have received a copy of the GNU Affero General Public License
  along with this program. If not, see <http://www.gnu.org/licenses/>.

  ----------------------------------------------------------------------------*/
#ifndef IO_HEADER
#define IO_HEADER

/*----------------------------------------------------------------------------*/
/* read a PGM image file
 */
double * read_pgm_image(char * name, int * X, int * Y);

/*----------------------------------------------------------------------------*/
/* read a 2D ASC format file
 */
double * read_asc_file(char * name, int * X, int * Y);

/*----------------------------------------------------------------------------*/
/* read an image from a file in ASC or PGM formats
 */
double * read_image(char * name, int * X, int * Y);

/*----------------------------------------------------------------------------*/
/* write curves into a PDF file. the output is PDF version 1.4 as described in
   "PDF Reference, third edition" by Adobe Systems Incorporated, 2001
 */
void write_curves_pdf( double * x, double * y, int * curve_limits, int M,
                       char * filename, int X, int Y, double width );

/*----------------------------------------------------------------------------*/
/* write curves into a TXT file
 */
void write_curves_txt( double * x, double * y, int * curve_limits, int M,
                       char * filename );

/*----------------------------------------------------------------------------*/
/* write curves into a SVG file
 */
void write_curves_svg( double * x, double * y, int * curve_limits, int M,
                       char * filename, int X, int Y, double width );

#endif /* !IO_HEADER */
/*----------------------------------------------------------------------------*/
