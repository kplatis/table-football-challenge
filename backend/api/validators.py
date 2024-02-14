

from typing import List, Optional

from fastapi import HTTPException


def validate_versus_team_ids(versus_team_ids: Optional[List[int]] = None):
    if versus_team_ids is not None:
        if len(versus_team_ids) != 2:
            raise HTTPException(
                status_code=400, detail="Two team IDs must be provided."
            )
        first_team_id_versus, second_team_id_versus = versus_team_ids
    else:
        first_team_id_versus, second_team_id_versus = None, None
    return first_team_id_versus, second_team_id_versus