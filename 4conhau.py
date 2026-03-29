import random


DEFAULT_POPULATION_SIZE = 80
DEFAULT_MAX_GENERATIONS = 2000
DEFAULT_MUTATION_RATE = 0.2
DEFAULT_TOURNAMENT_SIZE = 3
DEFAULT_ATTEMPTS = 5
# mỗi một con có có 1 cách đi khác nhau, nên tăng số lần chạy để có cơ hội tìm được nghiệm tối ưu hơn 50_80 là số trung bình chọn hợp lý.
# số thế hệ tối đa sẽ chạy không quá tối đa 2000 vòng lặp
# tỉ lệ đột biến 20% là hợp lý để duy trì sự đa dạng trong quần thể mà không làm mất đi quá nhiều tiến bộ đã đạt được.
# kích thước giải đấu 3 là một lựa chọn phổ biến, nó cung cấp sự cạnh tranh đủ để thúc đẩy tiến hóa mà không quá khắc nghiệt.
# thuật toán sẽ cahjy 5 lần mỗi lần có thể tìm random khác nhau, giúp tăng cơ hội tìm được nghiệm tối ưu hơn, đặc biệt là với các giá trị N lớn hơn.

def create_individual(size):
	"""Một cá thể ứng viên, trong đó chỉ số là hàng (row) và giá trị là cột (column)."""
	return [random.randint(0, size - 1) for _ in range(size)]
# Mỗi cá thể được tạo ra là một danh sách có độ dài bằng số lượng quân hậu (size), trong đó mỗi phần tử đại diện cho vị trí cột của quân hậu trên hàng tương ứng. 
# lặp lại size lần để tạo ra một cá thể hoàn chỉnh, mỗi lần chọn ngẫu nhiên một cột từ 0 đến size-1 cho quân hậu trên hàng đó.



def fitness(individual):
	"""Giá trị càng cao càng tốt. Fitness tối đa là n*(n-1)/2 khi không có cặp quân hậu nào tấn công nhau."""
	n = len(individual)
	# số quân hậu, kích thước của bàn cờ
	max_pairs = n * (n - 1) // 2
	# số cặp quân hậu tối đa xó thể có trên bàn cờ
	conflicts = 0
	# biến đếm số cặp quân hậu tấn công nhau được khởi tạo bằng 0 và sẽ được tăng lên mỗi khi tìm thấy một cặp quân hậu tấn công nhau.

	for r1 in range(n):
		# lặp qua từng dòng
		for r2 in range(r1 + 1, n):
			# lặp qua các dòng phía dưới dòng r1 để so sánh với quân hậu ở dòng r1
			c1, c2 = individual[r1], individual[r2]
			# lấy vị trí cột của quân hậu ở dòng r1 và r2
			same_column = c1 == c2
			# kiểm tra nếu hai quân hậu ở cùng một cột
			same_diagonal = abs(c1 - c2) == abs(r1 - r2)
			# kiểm tra nếu hai quân hậu nằm trên cùng một đường chéo bằng cách so sánh độ lệch cột với độ lệch hàng
			if same_column or same_diagonal:
				conflicts += 1
				# nếu hai quân hậu tấn công nhau, tăng biến đếm số cặp tấn công lên 1 

	return max_pairs - conflicts
# giá trị fitness được tính bằng cách lấy số cặp quân hậu tối đa trừ đi số cặp quân hậu tấn công nhau.
# giá trị fitness càng cao thì cá thể càng tốt, với giá trị tối đa là max_pairs khi không có cặp quân hậu nào tấn công nhau.


def tournament_selection(population, k=DEFAULT_TOURNAMENT_SIZE):
	"""Chon ca the tot nhat trong so k ca the duoc lay ngau nhien."""
	k = min(k, len(population))
	candidates = random.sample(population, k)
	return max(candidates, key=fitness)


def crossover(parent1, parent2):
	"""Lai ghep tai mot diem."""
	n = len(parent1)
	point = random.randint(1, n - 1)
	child1 = parent1[:point] + parent2[point:]
	child2 = parent2[:point] + parent1[point:]
	return child1, child2


def mutate(individual, mutation_rate=DEFAULT_MUTATION_RATE):
	"""Dot bien ngau nhien cot cua quan hau o moi hang theo ti le cho truoc."""
	n = len(individual)
	for row in range(n):
		if random.random() < mutation_rate:
			individual[row] = random.randint(0, n - 1)
	return individual


def genetic_algorithm(
	board_size,
	population_size=DEFAULT_POPULATION_SIZE,
	max_generations=DEFAULT_MAX_GENERATIONS,
	mutation_rate=DEFAULT_MUTATION_RATE,
	tournament_size=DEFAULT_TOURNAMENT_SIZE,
):
	population = [create_individual(board_size) for _ in range(population_size)]
	max_fit = board_size * (board_size - 1) // 2

	for generation in range(1, max_generations + 1):
		best = max(population, key=fitness)
		best_fit = fitness(best)

		if best_fit == max_fit:
			return best, generation

		next_population = [best[:]]

		while len(next_population) < population_size:
			p1 = tournament_selection(population, tournament_size)
			p2 = tournament_selection(population, tournament_size)
			c1, c2 = crossover(p1, p2)
			next_population.append(mutate(c1, mutation_rate))
			if len(next_population) < population_size:
				next_population.append(mutate(c2, mutation_rate))

		population = next_population

	best = max(population, key=fitness)
	return best, max_generations


def solve_n_queens_ga(
	n,
	attempts=DEFAULT_ATTEMPTS,
	population_size=DEFAULT_POPULATION_SIZE,
	max_generations=DEFAULT_MAX_GENERATIONS,
	mutation_rate=DEFAULT_MUTATION_RATE,
	tournament_size=DEFAULT_TOURNAMENT_SIZE,
):
	"""Chay GA nhieu lan va giu lai nghiem tot nhat tim duoc."""
	max_fit = n * (n - 1) // 2
	best_overall = None
	best_fit = -1
	best_generation = 0

	for _ in range(attempts):
		solution, generation = genetic_algorithm(
			board_size=n,
			population_size=population_size,
			max_generations=max_generations,
			mutation_rate=mutation_rate,
			tournament_size=tournament_size,
		)
		current_fit = fitness(solution)

		if current_fit > best_fit:
			best_overall = solution
			best_fit = current_fit
			best_generation = generation

		if current_fit == max_fit:
			return best_overall, best_generation, True

	return best_overall, best_generation, False


def print_board(solution):
	n = len(solution)
	for row in range(n):
		line = ["."] * n
		line[solution[row]] = "Q"
		print(" ".join(line))


if __name__ == "__main__":
	random.seed()

	try:
		n = int(input("Nhap N (so con hau): "))
	except ValueError:
		print("Gia tri N khong hop le.")
		raise SystemExit(1)

	if n < 1:
		print("N phai >= 1.")
		raise SystemExit(1)

	if n in (2, 3):
		print("Khong ton tai nghiem cho N = 2 hoac N = 3.")
		raise SystemExit(0)

	population_size = max(DEFAULT_POPULATION_SIZE, n * 20)
	max_generations = max(DEFAULT_MAX_GENERATIONS, n * 300)

	solution, gen, solved = solve_n_queens_ga(
		n,
		attempts=DEFAULT_ATTEMPTS,
		population_size=population_size,
		max_generations=max_generations,
	)
	fit = fitness(solution)
	max_fit = n * (n - 1) // 2

	if solved:
		print("Tim thay nghiem toi uu.")
	else:
		print("Chua tim thay nghiem toi uu, day la nghiem tot nhat tim duoc.")

	print("Nghiem tim duoc:", solution)
	print(f"So the he: {gen}")
	print(f"Fitness: {fit}/{max_fit}")
	print("Ban co:")
	print_board(solution)

