import seq2seq_att

model = seq2seq_att.Transliterator()
model.use_pretrained_model()  # use pre-trained model
output = model.decode_sequence('apple')  # strangely, without this code, transliterate() method raises error

def transliterate(input, detail=False, score=0.0):
	output = model.decode_sequence(input.strip())
	if detail:
		return jsonify({'input': input, 'output': output[0], 'score': float(output[1])})
	if output[1] >= score:
		return output[0]
	else:
		return None

if __name__ == '__main__':
	input = 'Orange'
	output = transliterate(input)
	print(f"{input}: {output}")
