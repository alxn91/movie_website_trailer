import fresh_tomatoes
import media
import api


troy = media.Movie(api.get_title("Troy"),
                   api.get_poster("Troy"),
                   "https://www.youtube.com/watch?v=znTLzRJimeY",
                   api.get_release_date("Troy"),
                   api.get_rating("Troy"))


batman_vs_superman = media.Movie(api.get_title("Man of Steel"),
                                 api.get_poster("Man of Steel"),
                                 "https://www.youtube.com/watch?v=DblEwHkde8U",
                                 api.get_release_date("Man of Steel"),
                                 api.get_rating("Man of Steel"))

step_brothers = media.Movie(api.get_title("Step Brothers"),
                            api.get_poster("Step Brothers"),
                            "https://www.youtube.com/watch?v=CewglxElBK0",
                            api.get_release_date("Step Brothers"),
                            api.get_rating("Step Brothers"))

the_man_who_knew_infinity = media.Movie(api.get_title("The Man Who Knew Infinity"),  # NOQA
                                        api.get_poster("The Man Who Knew Infinity"),  # NOQA
                                        "https://www.youtube.com/watch?v=oXGm9Vlfx4w",  # NOQA
                                        api.get_release_date("The Man Who Knew Infinity"),  # NOQA
                                        api.get_rating("The Man Who Knew Infinity"))  # NOQA

elf = media.Movie(api.get_title("Elf"),
                  api.get_poster("Elf"),
                  "https://www.youtube.com/watch?v=gW9wRNqQ_P8",
                  api.get_release_date("Elf"),
                  api.get_rating("Elf"))

ip_man = media.Movie(api.get_title("Ip Man"),
                     api.get_poster("Ip Man"),
                     "https://www.youtube.com/watch?v=1AJxXQ7xojE",
                     api.get_release_date("Ip Man"),
                     api.get_rating("Ip Man"))

movie = [troy,
         batman_vs_superman,
         step_brothers,
         the_man_who_knew_infinity,
         elf,
         ip_man]

fresh_tomatoes.open_movies_page(movie)
