# Нехай f(n) = 3n^2 - n + 4 та g(n) = n * log(n) + 5. Покажемо, що f(n) + g(n) = O(n^2):
#
# f(n) = 3n^2 - n + 4 є O(n^2), оскільки домінуючий член 3n^2.
#
# g(n) = n*log(n) + 5 є O(n*log n).
#
# Сума f(n) + g(n) = 3n^2 - n + 4 + n log(n) + 5 = O(n^2), оскільки n^2 домінує над n log(n).