/*
 * YaoEvalWire.h
 *
 */

#ifndef YAO_YAOEVALWIRE_H_
#define YAO_YAOEVALWIRE_H_

#include "BMR/Key.h"
#include "BMR/Gate.h"
#include "BMR/Register.h"
#include "GC/Processor.h"
#include "Auth/MAC_Check.h"

class YaoEvalWire : public Phase
{
public:
	typedef MAC_Check_Base<YaoEvalWire> MC;

	static string name() { return "YaoEvalWire"; }

	typedef ostream& out_type;
	static ostream& out;

	bool external;
	Key key;

	static YaoEvalWire new_reg() { return {}; }

	static void andrs(GC::Processor<GC::Secret<YaoEvalWire>>& processor,
			const vector<int>& args)
	{
		and_(processor, args, true);
	}
	static void ands(GC::Processor<GC::Secret<YaoEvalWire>>& processor,
			const vector<int>& args)
	{
		and_(processor, args, false);
	}
	static void and_(GC::Processor<GC::Secret<YaoEvalWire>>& processor,
			const vector<int>& args, bool repeat);

	static void inputb(GC::Processor<GC::Secret<YaoEvalWire>>& processor,
			const vector<int>& args);

	void set(const Key& key);
	void set(Key key, bool external);

	void random();
	void public_input(bool value);
	void op(const YaoEvalWire& left, const YaoEvalWire& right, Function func);
	void XOR(const YaoEvalWire& left, const YaoEvalWire& right);
	bool get_output();
};

#endif /* YAO_YAOEVALWIRE_H_ */
