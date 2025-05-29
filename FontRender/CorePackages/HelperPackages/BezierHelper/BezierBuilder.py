from .LinearBezier import LinearBezier
from .QuadraticBezier import QuadraticBezier
from .Point import Point

class BezierBuilder:
	def construct_beziers_from_points(first_point: Point, is_closed_curve: bool) -> list[LinearBezier|QuadraticBezier]:
		current_node = first_point
		previous_node = None

		beziers = []
		while current_node.has_next():
			if not(current_node.check_is_on_curve()):
				previous_node = current_node
				current_node = current_node.get_next()
				continue

			next_node = current_node.get_next()

			if next_node.check_is_on_curve():
				beziers.append(LinearBezier(current_node, next_node))
				previous_node = current_node
				current_node = current_node.get_next()
				continue

			if not(next_node.get_next().check_is_on_curve()):
				raise Exception("Sorry, invalid data")

			beziers.append(QuadraticBezier(current_node, next_node, next_node.get_next()))
			previous_node = current_node
			current_node = current_node.get_next()

		if not(is_closed_curve):
			return beziers

		if not(current_node.check_is_on_curve()) and not(first_point.check_is_on_curve()):
			raise Exception("Sorry, invalid data")

		if not(current_node.check_is_on_curve()):
			beziers.append(QuadraticBezier(previous_node, current_node, first_point))
			return beziers
		
		if not(first_point.check_is_on_curve()):
			beziers.append(QuadraticBezier(current_node, first_point, first_point.get_next()))
			return beziers

		beziers.append(LinearBezier(current_node, first_point))
		return beziers

	def insert_linear_bezier(beziers: list[LinearBezier|QuadraticBezier], insert_index: int, delta_x = None, delta_y = None) -> LinearBezier:
		if insert_index < 0 or insert_index > len(beziers):
			raise IndexError("Out of range")

		if len(beziers) == 0:
			beziers.insert(0, LinearBezier(Point(0,0,True), Point(0 + delta_x,0 + delta_y,True)))
			beziers[0].x0.update_next(beziers[0].get_x2())
			return
		
		x2 = Point(0,0,True)
		x0 = Point(0,0,True, x2)

		if insert_index > 0:
			x0 = beziers[insert_index - 1].get_x2()
			x2.update_next(x0.get_next())
			x0.update_next(x2)
			x2.update_x(x0.get_x() + delta_x)
			x2.update_y(x0.get_y() + delta_y)

		beziers.insert(insert_index, LinearBezier(x0,x2))

		return beziers[insert_index]

	def insert_quadratic_bezier(beziers: list[LinearBezier|QuadraticBezier], insert_index: int, delta_x = None, delta_y = None) -> QuadraticBezier:
		linear_bezier = BezierBuilder.insert_linear_bezier(beziers, insert_index, delta_x, delta_y)
		x1_x = (linear_bezier.x0.get_x() + linear_bezier.x2.get_x()) / 2
		x1_y = (linear_bezier.x0.get_y() + linear_bezier.x2.get_y()) / 2
		x1 = Point(x1_x, x1_y, False)
		quadratic_bezier = BezierBuilder.enhance_to_quadratic_bezier(linear_bezier, x1)
		beziers[insert_index] = quadratic_bezier
		return quadratic_bezier

	def reduce_to_linear_bezier(quadratic_bezier: QuadraticBezier) -> LinearBezier:
		quadratic_bezier.bezier_0.x0.update_next(quadratic_bezier.bezier_1.x2)
		return LinearBezier(quadratic_bezier.bezier_0.x0, quadratic_bezier.bezier_1.x2)

	def enhance_to_quadratic_bezier(linear_bezier: LinearBezier, x1: Point) -> QuadraticBezier:
		new_x1_point = Point(x1.get_x(), x1.get_y(), False, linear_bezier.x2)
		linear_bezier.x0.update_next(new_x1_point)
		return QuadraticBezier(linear_bezier.x0, new_x1_point, linear_bezier.x2)
