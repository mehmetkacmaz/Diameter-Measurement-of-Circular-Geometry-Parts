/*----------------------------------------------------------------------------

  Implementation of Canny/Devernay's sub-pixel edge detector.

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
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "io.h"
#include "devernay.h"

/*----------------------------------------------------------------------------*/
/* print usage and exit
 */
static void usage(void)
{
  fprintf(stderr,"devernay %s\n",DEVERNAY_VERSION);
  fprintf(stderr,"Copyright (c) 2016-2017 ");
  fprintf(stderr,"Rafael Grompone von Gioi and Gregory Randall\n\n");
  fprintf(stderr,"usage: devernay <image> [-s S] [-h H] [-l L] [-w W] [-t T] ");
  fprintf(stderr,"[-p P] [-g G]\n\n");
  fprintf(stderr,"image  PGM or ASC file formats are handled\n");
  fprintf(stderr,"-s S   set the blur standard deviation ");
  fprintf(stderr,"(default S=0.0 -> no blurring)\n");
  fprintf(stderr,"-h H   set high threshold (default H=0.0)\n");
  fprintf(stderr,"-l L   set low threshold (default L=0.0)\n");
  fprintf(stderr,"-w W   set line width in PDF and SVG to W (default W=1.3)\n");
  fprintf(stderr,"-t T   write TXT output to file T\n");
  fprintf(stderr,"-p P   write PDF output to file P\n");
  fprintf(stderr,"-g G   write SVG output to file G\n\n");
  fprintf(stderr,"examples: devernay image.pgm -p output.pdf\n");
  fprintf(stderr,"          devernay image.pgm -t output.txt -p output.pdf ");
  fprintf(stderr,"-g output.svg\n");
  fprintf(stderr,"          devernay image.pgm -p output.pdf ");
  fprintf(stderr,"-s 1.0 -l 5.0 -h 15.0 -w 0.5\n");

  exit(EXIT_FAILURE);
}

/*----------------------------------------------------------------------------*/
/* get an optional parameter from arguments

   if found, the value is returned and it is removed from the list of arguments.
   adapted from pick_option by Enric Meinhardt-Llopis.

   example: if arguments are "command -p 123 input.txt",
            char * p = get_option(&argc,&argv,"-p","0");
            will give "123" in p and leave arguments as "command input.txt"
 */
static char * get_option(int * argc, char *** argv, char * opt, char * def)
{
  int i,j;

  for(i=0; i<(*argc-1); i++) /* last argument cannot have an optional value */
    if( strcmp( (*argv)[i], opt ) == 0 )  /* option opt found */
      {
        char * r = (*argv)[i+1];     /* save the optional value to return   */
        for(j=i; j < (*argc-2); j++) /* shift arguments to remove opt+value */
          (*argv)[j] = (*argv)[j+2];
        *argc -= 2;     /* decrease the number of arguments in 2, opt+value */
        return r;  /* return the value found for option opt */
      }
  return def; /* option not found, return the default value */
}

/*----------------------------------------------------------------------------*/
/*                                    main                                    */
/*----------------------------------------------------------------------------*/
int main(int argc, char ** argv)
{
  double * image;      /* image of size X,Y */
  double * x;          /* x[n] y[n] coordinates of result contour point n */
  double * y;
  int * curve_limits;  /* limits of the curves in the x[] and y[] */
  int X,Y,N,M;         /* result: N contour points, forming M curves */
  char * txt_out = get_option(&argc,&argv,"-t",NULL);  /* txt filename    */
  char * pdf_out = get_option(&argc,&argv,"-p",NULL);  /* pdf filename    */
  char * svg_out = get_option(&argc,&argv,"-g",NULL);  /* svg filename    */
  double S = atof(get_option(&argc,&argv,"-s","0.0")); /* default sigma=0 */
  double H = atof(get_option(&argc,&argv,"-h","0.0")); /* default th_h=0  */
  double L = atof(get_option(&argc,&argv,"-l","0.0")); /* default th_l=0  */
  double W = atof(get_option(&argc,&argv,"-w","1.3")); /* default W=1.3   */

  /* read input */
  if( argc != 2 ) usage();
  image = read_image(argv[1],&X,&Y);

  /* call Canny/Devernay algorithm */
  devernay(&x, &y, &N, &curve_limits, &M, image, X, Y, S, H, L);

  /* write required outputs, TXT and/or PDF */
  if( txt_out != NULL ) write_curves_txt(x,y,curve_limits,M,txt_out);
  if( pdf_out != NULL ) write_curves_pdf(x,y,curve_limits,M,pdf_out,X,Y,W);
  if( svg_out != NULL ) write_curves_svg(x,y,curve_limits,M,svg_out,X,Y,W);

  /* free memory */
  free( (void *) image );
  free( (void *) curve_limits );
  free( (void *) x );
  free( (void *) y );

  return EXIT_SUCCESS;
}
/*----------------------------------------------------------------------------*/
