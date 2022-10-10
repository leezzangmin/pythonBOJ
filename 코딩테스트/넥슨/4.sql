select party, count(cand.party) 'Party Seats_won' from candidates as cand
inner join 
(select r.constituency_id, r.candidate_id from results r
inner join 
(select constituency_id,max(votes) mm from results group by constituency_id) t 
on r.votes=t.mm and r.constituency_id=t.constituency_id) res
on res.candidate_id=cand.id
group by party
order by count(cand.party) desc;
