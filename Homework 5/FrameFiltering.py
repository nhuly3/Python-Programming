filtered = frame.filter(frame['ocean_proximity'].is_in(["NEAR BAY", "NEAR OCEAN", "INLAND"]))
lazy_frame=filtered.lazy()
print(lazy_frame.explain())
