#!/usr/bin/python

import random

ANSIBLE_METADATA = {
    'metadata_version': '1.1',
    'status': ['preview'],
    'supported_by': 'community'
}

DOCUMENTATION = '''
---
module: real_facts

short_description: A module that dishes out the true facts.

version_added: "2.8"

description:
    - "A module that dishes out the true facts."
    - "This is an ansible implementation of the GNU Octave 'truth' script."
    - "https://fossies.org/linux/octave/scripts/miscellaneous/fact.m"

options:
    name:
        description:
            - This is the message to send to the sample module
        default: Richard Stallman

author:
    - David Newswanger (@newswangerd)
'''

EXAMPLES = '''
# Pass in a message
- name: Test with a message
  real_facts:
    name: David Newswanger
'''

RETURN = '''
fact:
    description: Actual facts
    type: str
'''

from ansible.module_utils.basic import AnsibleModule


FACTS = [
    "{name} takes notes in binary.",
    "{name} doesn't need sudo. I will make him a sandwich anyway.",
    "{name} is my shephurd, and I am his GNU.",
    "{name} doesn't wget, {name} wdemands!",
    "{name} can touch MC Hammer.",
    "{name} doesn't read web pages. They write to him.",
    "{name} gets 9 bits to the byte.",
    "{name} doesn't really believe in open software, because it's not free enough.",
    "{name} can leave neutral or negative feedback on eBay.",
    "{name} is the only man alive who can pronounce GNU the way it is meant to be pronounced.",
    "{name} does not own a mobile phone because he can fashion a crude convex dish and shout into it at the exact resonant frequency of the ozone, causing a voice to seemingly come from the sky above his intended recipient.",
    "{name} is so handsome that when he was young he was responsible for all other geeks not being able to get girls. This is why he has to cover his face with a thick layer of hair.",
    "Some people check their computers for viruses. Viruses check their computers for {name}.",
    "{name} memorises all his documents. In binary. He just types everything in whenever he needs a document.",
    "When {name} makes a sudo command, he loses permissions.",
    "{name}'s beard is made of parentheses.",
    "{name}'s DNA is in binary.",
    "{name}'s nervous system is completely wireless.",
    "{name}'s brain accepts UNIX commands.",
    "If {name} has 1 GB of RAM, and if you have 1 GB of RAM, {name} has more RAM than you.",
    "{name} eats ethernet cables. That's why they invented wireless.",
    "{name} has a katana. 'Nuff said.",
    "{name} wrote a program that divides by zero.",
    "{name} doesn't use zip drives, he just squeezes the hard drive.",
    "{name}'s compiler is afraid to report errors.",
    "{name} wrote the compiler God used. The Big Bang was the Universe's first segfault.",
    "{name} successfully compiled a kernel of popcorn.",
    "{name} doesn't write programs, they write themselves out of reverence.",
    "{name} can make infinite loops end.",
    "{name}'s anti-virus programs cures HIV.",
    "{name}'s computer doesn't have a clock, it defines what time it is.",
    "{name} wrote a program to compute the last digit of pi.",
    "{name} doesn't use web browsers. He sends a link to a daemon that uses wget to fetch the page and sends it back to him.",
    "{name} can solve the halting problem... in polynomial time.",
    "For {name}, polynomial time is O(1).",
    "{name} didn't \"write\" Emacs or created it in his own image. {name} made Emacs an instance of himself.",
    "{name} can coerce meaningful data from /dev/null.",
    "Some people wear Linus Torvalds pyjamas to bed, Linus Torvalds wears {name} pyjamas.",
    "There is no software development process, only a bunch of programs {name} allows to exist.",
    "{name} spends his leisure time programming with Guile on GNU Hurd.",
    "{name}'s left and right hands are named \"(\" and \")\" ",
    "{name} first words were actually syscalls.",
    "{name} didn't create the singularity. He is the singularity. GNU/Linux is only the event horizon.",
    "When {name} pipes to more, he gets less ",
    "{name} never showers, he runs 'make clean'.",
    "{name} needs neither mouse nor keyboard to operate his computer. He just stares it down until it does what he wants.",
    "{name} didn't write the GPL. He is the GPL.",
    "{name}'s pinky finger is really a USB memory stick.",
    "{name} called his operating system GNU because he created it before computers existed, when actual gnus were used for calculations.",
    "In Soviet Russia, {name} is still {name}!",
    "{name}'s flute only plays free music.",
    "When {name} uses floats, there are no rounding errors.",
    "{name} wrote a program so powerful it knows the question to 42.",
    "{name} released his own DNA under GNU FDL.",
    "{name} knows the entire Wikipedia by heart, markup included.",
    "{name} wrote the HAL9000 OS.",
    "{name}'s laser pointer is a lightsaber.",
    "{name} never steps down, he shifts the universe up.",
    "{name} doesn't maintain code, he stares at it until it fixes itself out of reverence.",
    "{name} doesn't use an editor, he sets the fundamental constants of the universe so that a magnetic platter with his code on it evolves itself.",
    "{name} doesnâ€™t code, he dares the computer to not do his bidding.",
    "Global warming is caused by {name}'s rage towards non-free software.",
    "Rather than being birthed like a normal child, {name} instead instantiated himself polymorphically. Shortly thereafter he grew a beard.",
    "{name} discovered extra-terrestrial life but killed them because they distributed non-free software.",
    "{name} doesn't evaluate expressions, expressions evaluate to {name}.",
    "{name} can see Russia from his house.",
    "{name} proved P=NP, twice!",
    "{name} knows of an unfixed bug in TeX.",
    "{name} can write a context-free grammar for C.",
    "{name} can determine whether an arbitrary program will terminate.",
    "{name}'s computer has only two buttons. One is for guests.",
    "{name} does not actually write programs. He comes up with a length and digit index in pi.",
    "{name}'s distributed version control system is a flamewar on Usenet.",
    "{name} wrote the first version of Emacs on a typewriter.",
    "{name} has no known weaknesses, except for a phobia against soap.",
    "{name} is not affected by Godwin's Law.",
    "{name} can write an anti-virus program that cures HIV. Too bad he never writes anti-virus programs.",
    "{name}' facial hair is \"free as in beard\"",
    "{name} is licensed under GPL, so you can clone him and redistribute copies so you can help your neighbor. For example a version that take a bath more often.",
    "{name} doesn't code, he just travels around the world.",
    "{name} was coded by himself in lisp with Emacs.",
    "{name} doesn't eat McDonald's because the machine that kills the cows uses proprietary software.",
    "There is no chin behind {name}'s legendary beard, there is only another Emacs.",
    "In an average living room there are 1,242 objects {name} could use to write an OS, including the room itself.",
    "Vendor lock-in is when vendors lock themselves inside of a building out of fear of {name}'s wrath.",
    "When {name} executes ps -e, you show up.",
    "When {name} gets angry he doesn't swear, he recurses.",
    "On {name}'s computer the bootloader is contained in his .emacs.",
    "{name} can make any operating system free, free from drivers.",
    "{name} programmed Chuck Norris.",
    "Behind {name}'s beard there is another fist, to code faster.",
    "{name} won a Sudoku that started with only one number in each line.",
    "{name}'s brain compiles and runs C code.",
    "{name} wrote the first version of Emacs using Emacs.",
    "{name} never gonna give you up, never gonna let you down, never gonna run around and desert you, never gonna make you cry, never gonna say goodbye, never gonna tell a lie and hurt you.",
    "{name}, upon reading these facts, didn't laugh at all. Instead, he complained that he is being linked to that dirty \"open source\" software. He also asked it to be changed to \"free software\", in order to raise awareness for software freedom in our society.",
    "{name} has no problem using Emacs. He wrote it with his 4 hands.",
    "{name} will revert the big rip by adding parenthesis to the dark matter.",
    "When you make a Google search and it doesn't find the answer, Google gently consults {name}.",
    "{name}'s uptime is over 53 years. And counting up.",
    "{name}'s portable music player can play ogg and WMA, but is too afraid to invoke {name}'s wrath by playing WMA. Ogg it is, then.",
    "{name} will never die, but may some day go to /dev/null.",
    "{name} once got swine flu, but it got cleansed by hereditary GPL and thus got assimilated.",
    "{name} don't cut his hair because there are no GNU/Scissors.",
    "{name} is the one who trims Chuck Norris beard. And he does it freely, of course.",
    "{name} does not take bath, for the hydroelectric company uses proprietary software.",
    "Agent Smith loves {name}'s scent.",
    "{name} is the One.",
    "\"They can take our lives, but they can never take our freedom.\" -- William Wallace after a little talk with {name}.",
    "{name} can connect to any brain using an Emacs ssh client.",
    "{name} ported Emacs to Intel 4004 chip.",
    "{name} did not write GNU Emacs, he simply read the source code from /dev/null.",
    "{name} once used GDB to reverse-engineer Windows 7 into a free operating system - able to run on GNU Emacs!",
    "{name} does not contribute to open source projects, open source projects contribute to {name}, and then call themselves free software projects.",
    "{name} programmed himself before he could even exist",
    "{name} can fill up /dev/null.",
    "{name} is so zealous about privacy he has /dev/null as his home.",
    "When {name} runs /bin/false, it returns \"true\".",
    "{name} doesn't like money, because banks don't run on free software.",
    "{name} uses GNU tar to compress air.",
    "When {name} reports a bug, the bug prefers to squash itself instead of facing {name}'s wrath.",
    "There are no Windows in {name}'s house... only Doors...",
    "{name} doesn't like neither PCs-Intel nor Burger King... He prefers e-Macs...",
    "{name} can use grep to find Jimmy Hoffa.",
    "{name} made it possible to not absolutely abhor HPUX.",
    "When {name} pours his alphabets cereal into a bowl, only G's, N's, and U's come out.",
    "{name} is pronounced \"GNU slash Stallman\"",
    "{name} doesn't mind if you read his mail as long as you don't delete it before he reads it.",
    "{name} is just a guy who has strong principles and decided to follow them.",
    "{name} knows that you don't have class because it is a keyword that he defined.",
    "{name} doesn't need a qwerty/dvorak keyboard only two buttons \"1\" and \"0\" and his erect penis.",
    "On the first day {name} said M-x create-light.",
    "{name} once went out of scope for a while. The garbage collector never dared to touch him.",
    "{name} does not compile, he closes his eyes, and see energy lines created between bit blocks by the compiler optimizations.",
    "intx80 first calls {name} before calling sys_call.",
    "Tron is actually a biographical story about {name}. The director decided to tone it down or audiences wouldn't find it believable.",
    "{name} always wears a red shirt to make sure that whatever attacks his away-team has to go through him first.",
    "kill -9 invokes {name}'s rage against a process.",
    "If Richard were to stumble upon stallmanfacts.com, he would find it a gnuisance.",
    "{name} can telnet into Mordor.",
    "sudo chown Richard:Stallman /all/your/base",
    "{name}'s nervous system is completely wireless.",
    "{name} does not sleep. He yields.",
    "Some people say M-x psychoanalyse-pinhead is a merely a program. Others say M-x psychoanalyse-pinhead *is* {name}. All I know is, {name} is The Stig.",
    "If you execute Emacs backward it either undoes the industrial revolution or induces the rapture. But only {name} knows which.",
    "If {name}'s beard were ever trimmed, the clippings would re-marshal into an exact copy of {name}.",
    "{name} never sleeps because he altered his own source to gain background garbage collection.",
    "{name}'s doctor can retrieve a blood sample via CVS.",
    "{name} can touch this.",
    "Because {name}'s DNA is licensed under the FDL, his doctor can't draw his blood without violating HIPAA.",
    "{name} can remove his own appendix, using only GDB.",
    "{name}'s DNA includes debugging symbols. But he doesn't need them.",
    "{name} met Chuck Norris once. Chuck tried a roundhouse, but Richard bashed him in the skull.",
    "{name} doesn't need to buy a bigger hard drive. He can compress data infinitely.",
    "When {name} cannot take your call, his beard answers the phone for you.",
    "The R in RMS stands for RMS.",
    "{name} can parse HTML with regular expressions.",
    "{name}'s traceroute goes all the way through an infinite number of anonymous proxies back to the traffic's source.",
    "{name}'s beard is in fact not a just a beard, but a microprinted hard copy of Emacs source code. New patches must be checked against new hair growth before being approved.",
    "In the beginning-of-buffer there was {name}.",
    "The NOOP was created to give {name} some time to comb his beard.",
    "Whenever {name} looks at a Windows computer, it segfaults. Whenever {name} doesn't look at a Windows computer, it segfaults.",
    "{name} can walk on Windows!",
    "After being unable to satisfy my wife for years, {name} was able to single-handedly unlock her orgasm within seconds and managed to write a texinfo manual minutes later for other users.",
    "{name}'s tabbed browser is a set to wget/telnet fg/bg processes.",
    "There is no chin under {name}' beard. There's only another beard. Recursively.",
    "{name} can chown anything! stallman@stallman~$ chown stallman:stallman Earth (for example)",
    "{name} freed his beard so he can always check what's in it.",
    "In the beginning was the Word, and the Word was with RMS, and the Word was GNU.",
    "RMS means \"RMS means Stallman\"",
    "{name} is the babelfish of his own speeches.",
    "{name} wrote his own library and lives in it.",
    "{name} found Waldo using grep in /dev/null",
    "{name} doesn't sleep, he is compiling.",
    "{name} will get Coca Cola to release their recipe under the GPL.",
    "{name} doesn't change clothes. He makes case mods.",
    "{name} compiled the first version of gcc with an hexadecimal editor.",
    "{name} will be the last guest on Linux Outlaws.",
    "{name} calculates the universe's entropy by exploiting forced stack overflows.",
    "{name}'s consciousness will one day become the singularity, which will create Deep Thought, and answer the meaning of life, the universe and everything.",
    "C is actually written in RMS.",
    "{name} can write software that does not have a buffer overflow when counting money lost by Jerome Kerviel.",
    "There were no double rainbows before {name}.",
    "Chuck Norris had to shorten his beard in the presence of {name} because two beards that awesome, so close would segfault the universe (again).",
    "RMS is Titanic.",
    "{name} is the answer to the Turing Test.",
    "{name}'s beard makes ads for Gillette and Braun appear.",
    "for i = 1 to Stallman will never stop.",
    "\"RMS\" stands for \"RMS Makes Software\"",
    "Whenever someone writes a \"Hello, world\" program, {name} says \"Hello\" back.",
    "{name} wasn't born. He was compiled from source.",
    "{name} has a URL tattooed on the left side of his chest where you can download his genetic code.",
    "The GNU command line idiom that {name} never needs: \"date | more\"",
    "{name}'s toe cheese is aged to perfection.",
    "{name} doesn't always run an OS kernel, but when he does he prefers GNU/Hurd. He is... the most interesting hacker in the world. Stay free, my friends.",
    "When {name} gets hungry, he just picks debris from his foot and eats it.",
    "{name} can GPL your code just by looking at it funny.",
    "{name} loves birds. Birds make auricular love to {name}.",
    "{name} is so free that the primitive recursive function for computing his liberty causes a stack overflow.",
    "GNU Hurd is taking more than twenty years to develop because {name} is using a programming language comprised entirely of different lengths of time.",
    "{name}'s beard contains {name}, whose beard contains {name}....",
    "{name} could have had a Google Plus account in 2010. Too bad he didn't want it.",
    "{name} pipes the Emacs binaries to /dev/dsp before he goes to sleep.",
    "When {name} counted his fingers as a kid, he always started with 0.",
    "When {name}'s computer gets a virus, he simply applies a GPL license to it which converts the whole botnet to Linux. I mean, GNU/Linux.",
    "{name}'s beard trimmings can cure cancer. Too bad he never shaves.",
    "{name}'s doesn't kill a process, he just dares it to stay running.",
    "{name} exists because he compiled himself into being.",
    "{name}'s first words were in binary. When they couldn't understand him, he wrote a parser.",
    "{name} doesn't need any codecs, he just opens a multimedia file with Emacs, and reads the bytes of the file as plain text. He then performs all the necessary decoding in his mind. But he refuses to decode files encrypted with DRM, although his mind is able to.",
    "{name} was right. Sadly.",
    "{name} can wiretap the NSA.",
    "This is how {name} created Emacs: http://stallman.org/photos/rms-working/img_0631.jpg",
    "Join {name} now and share the software, you'll be a free hacker, you'll be free!",
    "{name} has not agreed to the terms and conditions and privacy policy because only he can actually read all of it.",
    "{name} knows how of a backdoor to AES, but he respects your freedom and privacy too much to actually use it.",
    "{name} will never get tired of being mocked for the foot cheese incident.",
    "You like to release non-free software around {name}? I too like to live dangerously...",
    "Yeah, if could just go ahead and make all software free for {name}, that'd be great, thanks.",
    "{name} knows exactly what you mean when you talk about the cloud. But do you?",
    "{name} satisfies Greenspun's Tenth Rule of programming, since his DNA also contains a complete implementation of all of Common Lisp.",
    "{name} can violate the GPL. In a vulgar display of power, he once did so with the Emacs source code, but he undid the violation before most people noticed.",
    "Good guy {name} does not try to shake you down for money. He will just kindly ask you to comply with the GPL.",
    "{name} is in fact also a little sad that Steve Jobs is gone because it has diminished the size of the loyal opposition.",
    "{name} can release LLVM and clang under the GPL.",
    "No, really, {name} has a katana.",
    "Every day {name} finds at least fifteen things in the world to rage about. You can read his findings here: http://stallman.org/archives/polnotes.html"
    "Some of these {name} facts are completely true. Seriously.",
]


def run_module():
    # define available arguments/parameters a user can pass to the module
    module_args = dict(
        name=dict(type='str', default='Richard Stallman'),
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    result = dict(
        changed=False,
        fact=''
    )

    result['fact'] = random.choice(FACTS).format(
        name=module.params['name']
    )

    if module.check_mode:
        return result

    module.exit_json(**result)


def main():
    run_module()


if __name__ == '__main__':
    main()
